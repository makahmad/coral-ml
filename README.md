# coral image processing

### To create model/graph
  - Install docker
  - Install tensorflow image: ```docker run -it gcr.io/tensorflow/tensorflow:latest-devel```
  - Exit docker by typing exit then create a folder in `$Home` called `tf_files`
  - Create a folder called photos within `tf_files` folder
  - Place all images in species labeled folder under the photos folder
  - Open terminal and link images to docker instance: ```docker run -it -v $HOME/tf_files:/tf_files gcr.io/tensorflow/tensorflow:latest-devel```
  - Get the latest training code:
    - ```cd /tensorflow```
    - ```git pull```
- Run training:
  - ```python tensorflow/examples/image_retraining/retrain.py --bottleneck_dir=/tf_files/bottlenecks --model_dir=/tf_files/inception --output_graph=/tf_files/retrained_graph.pb --output_labels=/tf_files/retrained_labels.txt --image_dir /tf_files/photos```
  - Grab the `retrained_graph.pb` and `retrained_labels.txt` files from `$Home/tf_files/` and place into `/Users/PROJECT`


### To classify
- Put all images to be classified in a folder called upload under `/Users/PROJECT`
- Open terminal
- Go to `/Users/PROJECT`
- Run the following commands:
  - ```source ./tfenv/bin/activate```
  - ```python cnn_classify.py```
- The program 
- moves the images to a folder named after the coral species name
- Inserts two rows per image in the `coral.db` sqlite db: one row for highest scored species and another row for second highest score distinguished by a column called rank. Other db columns are as follows:
    - File: name of the file
    Species: name of the species
    - Date: date of the classification
    - Score: confidence level in percent decimal format
    - Rank: 1 for highest confidence, 2 for second highest confidence
- deactivate
