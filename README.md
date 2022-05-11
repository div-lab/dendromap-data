# DendroMap Data

This repository contains the data used in the [live site](https://div-lab.github.io/dendromap/) for DendroMap. This readme contains instructions for accessing the data and using your own data.

### Accessing the Data

The file structure is specified used in this repository defines how our program uses the data. For example for the CIFAR-10 dataset from ResNet50 activations the file structure is the following:

📦 cifar10
┣ 📂 clusters
┃ ┣ 📜 cifar10_resnet50.json
┃ ┗ 📜 cifar10_resnet50_classes.json
┣ 📂 images
┃ ┣ 📜 test-0.png
┃ ┣ 📜 test-1.png
...  
┗ ┗ 📜 test-9999.png

You can specify where the files are located through an object of the following format:

```javascript
{
	dataset: "CIFAR-10",
	model: "ResNet-50",
	cluster_filepath: "https://div-lab.github.io/dendromap-data/cifar10/clusters/cifar10_resnet50.json",
	class_cluster_filepath: "https://div-lab.github.io/dendromap-data/cifar10/clusters/cifar10_resnet50_classes.json",
	image_filepath:"https://div-lab.github.io/dendromap-data/cifar10/images",
}
```

By adding this to the array of objects in the _options_ array in `src/main.js` in the User Interface Code, you add another option to the dropdown menu for you to use.

### Using your own Data

You can generate your own data using python functions we created in the [dendromap-notebooks](https://github.com/div-lab/dendromap-notebooks) repository. The notebooks that generated the datafiles in this repository also live there as examples.

Once you've generated your own files, put them in the `public` folder in the Svelte User Interface Code, then add another option in `src/main.js` just like in the previous example.

```javascript
{
	dataset: "YOUR DATASET NAME",
	model: "YOUR MODEL NAME",
	cluster_filepath: "CLUSTER_FILEPATH",
	class_cluster_filepath: "CLASS_CLUSTER_FILEPATH/OPTIONAL",
	image_filepath: "IMAGE_FILEPATH",
}
```

The `class_cluster_filepath` is optional and will allow for class filtering if it is present. For example, it is not present in VAE and MNIST dataset.
