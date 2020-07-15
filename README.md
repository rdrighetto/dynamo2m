# dynamo2m
`dynamo2m` is a set of Python scripts to interface the subtomogram averaging software 
[Dynamo](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Main_Page) 
with the 
multi particle refinement cryo-EM software [M](http://www.warpem.com/warp/?page_id=1614).

It forms part of the image processing pipeline described in the following [preprint]().


## Motivation
Dynamo is a tomography specific software package with many useful tools for subtomogram averaging including...

- Flexible [subtomogram averaging](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Dcp_GUI) workflows
- Ways to [visualise](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Walkthrough_for_lattices_on_vesicles#Merging_the_tables) subtomogram averaging results
- Interactive tools for [initial model generation](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Starters_guide#Initial_model_generation)
- [Automated tilt-series alignment](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Walkthrough_on_command_line_based_tilt_series_alignment)
- [PCA based classification and analysis tools](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Walkthrough_on_PCA_through_the_command_line)
- [Geometric modelling and visualisation tools](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Model) for particle picking and tomogram annotation
- much much more...

M is an imaging modality

## Scripts
- `dynamo2warp` for the conversion of Dynamo metadata to facilitate extraction of particles in Warp
- `warp2dynamo` for the conversion of Warp STAR files into Dynamo compatible metadata
- Conversion to Excel speadsheet (.xlsx)


## Installation
Installation is available directly from the [Python package index](https://pypi.org/project/dynamo2m/)
```
pip install starfile
```


## Usage