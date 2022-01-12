==========================================================
Data Repository
==========================================================
Source code and data files for the manuscript Role of oxygen states in low valence nickelates. Execute plot.ipynb to view the data.

How to cite
-----------
If this data is used, please cite Role of oxygen states in low valence nickelates Y. Shen, J. Sears, G. Fabbris, J. Li, J. Pelliciari, I. Jarrige, Xi He, I. Bozovic, M. Mitrano, Junjie Zhang, J. F. Mitchell, A. S. Botana, V. Bisogni, M. R. Norman, S. Johnston, M. P. M. Dean

The discovery of superconductivity in square planar low valence nickelates has ignited a vigorous debate regarding their essential electronic properties: Do these materials have appreciable oxygen charge-transfer character akin to the cuprates or are they in a distinct Mott-Hubbard regime where oxygen plays a minimal role? Here, we resolve this question using O K-edge Resonant Inelastic X-ray Scattering (RIXS) measurements of the low valence nickelate La4Ni3O8 and a prototypical cuprate La2−xSrxCuO4 (x = 0.35). As expected, the cuprate lies deep in the charge-transfer regime of the Zaanen-Sawatzky-Allen (ZSA) scheme. The nickelate, however, is not well-described by either limit of the ZSA scheme and is found to be of mixed charge-transfer / Mott-Hubbard character with the Coulomb repulsion U of similar size to the charge transfer energy ∆. Nevertheless, the transition-metal-oxygen hopping is larger in La4Ni3O8 than in La2−xSrxCuO4, leading to a significant superexchange interaction and an appreciable hole occupation of the ligand O orbitals in La4Ni3O8 despite its larger ∆. Our results clarify the essential characteristics of low valence nickelates and put strong constraints on theoretical interpretations of superconductivity in these
materials.

Run locally
-----------

Work with this by installing `docker <https://www.docker.com/>`_ and pip and then running

.. code-block:: bash

       pip install jupyter-repo2docker
       jupyter-repo2docker --editable .

Change `tree` to `lab` in the URL for JupyterLab.

Run remotely
------------

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/mpmdean/Shen2022role/HEAD?filepath=plot.ipynb
