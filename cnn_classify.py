import tensorflow as tf, sys
import sqlite3, os


conn = sqlite3.connect('corals.db')
c = conn.cursor()

# Create table
try:
    c.execute('''CREATE TABLE corals
                 (file text, species text, date text, score real, rank integer)''')
except sqlite3.OperationalError:
    pass


# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')


# Open a file
path = "upload"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
    if os.path.isfile(os.path.join(path, file)) and file[:1] != ".":
        # Read in the image_data
        image_data = tf.gfile.FastGFile(path+'/'+file, 'rb').read()

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, \
                                   {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            i = 0
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                # print('%s (score = %.5f)' % (human_string, score))

                if i < 2:
                    c.execute(
                        "INSERT INTO corals VALUES ('" + file + "','" + human_string + "',date('now','localtime'), " + str(
                            float(score)) + ","+str(int((i+1)))+")")
                    i += 1
                    if i==1:
                        if not os.path.exists(path + "/" + human_string):
                            os.makedirs(path + "/" + human_string)
                        os.rename(path + "/" + file, path + "/" + human_string + "/" + file)


# Save (commit) the changes
conn.commit()

for row in c.execute('SELECT * FROM corals'):
    print row

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()