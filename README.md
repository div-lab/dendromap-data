# DendroMap Data

This repository contains the data used in the [DendroMap Live Site](https://div-lab.github.io/dendromap/). For use with your own data, keep reading, then navigate to [DendroMap Notebooks](https://github.com/div-lab/dendromap-notebooks) for example code.

## Using your own Data

To give an example, if I downloaded the cifar10 data from this repository, I would put the cifar10 folder in the `public` folder in my local server in the [DendroMap Code](https://github.com/div-lab/dendromap).

I would then connect the data to [DendroMap Code](https://github.com/div-lab/dendromap) by adding an object in the options array inside of `src/dataOptions.js`. It must have the following format:

```javascript
{
	dataset: "YOUR DATASET NAME",
	model: "YOUR MODEL NAME",
	cluster_filepath: "CLUSTER_FILEPATH",
	class_cluster_filepath: "CLASS_CLUSTER_FILEPATH**OPTIONAL**",
	image_filepath: "IMAGE_FILEPATH",
}
```

In the case of the cifar10 data in this repository,

```text
📦 cifar10
┣ 📂 clusters
┃ ┣ 📜 cifar10_resnet50.json
┃ ┗ 📜 cifar10_resnet50_classes.json
┣ 📂 images
┃ ┣ 📜 test-0.png
┃ ┣ 📜 test-1.png
...
┗ ┗ 📜 test-9999.png
```

since it has this file structure, I would connect it by adding this object:

```javascript
{
	dataset: "CIFAR-10",
	model: "ResNet50",
	cluster_filepath: "cifar10/clusters/cifar10_resnet50.json",
	class_cluster_filepath: "cifar10/clusters/cifar10_resnet50_classes.json",
	image_filepath: "cifar10/images",
}
```

Then this option will show up in the dataset selection dropdown in the user interface.

You can generate your own data using python functions we created in the [DendroMap Notebooks](https://github.com/div-lab/dendromap-notebooks) repository. The notebooks that generated the datafiles in this repository also live there as examples.

Once you've generated your own files, put them in the `public` folder in the [DendroMap Code](https://github.com/div-lab/dendromap), then add another option in `src/dataOptions.js` as shown above with the cifar10 example.

## Links

-   [DendroMap Live Site](https://div-lab.github.io/dendromap/)
-   [DendroMap Paper](https://arxiv.org/) change this
-   [DendroMap Code](https://github.com/div-lab/dendromap)
-   [DendroMap Data](https://github.com/div-lab/dendromap-data) (**you are here**)
-   [DendroMap Notebooks](https://github.com/div-lab/dendromap-notebooks)
