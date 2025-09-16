import requests

import nglview
from nglview.base_adaptor import Structure
from nglview.widget import NGLWidget

class PdbIdStructure(Structure):

    def __init__(self, pdbid, mirror=None):
        super().__init__()
        self.pdbid = pdbid
        self.mirror = mirror
        self.ext = "cif"
        self.params = {}

    def get_structure_string(self):
        if self.mirror and self.mirror.lower() == 'pdbe':
            url = "https://www.ebi.ac.uk/pdbe/entry-files/download/" + self.pdbid + ".cif"
        elif self.mirror and self.mirror.lower() == 'pdbj':
            url = "https://data.pdbj.org/pub/pdb/data/structures/divided/mmCIF/" + self.pdbid[1:3] +"/" + self.pdbid + ".cif"
        else:
            url = "http://www.rcsb.org/pdb/files/" + self.pdbid + ".cif"
        return requests.get(url).text


def show_pdbid(pdbid, mirror=None, **kwargs):
    '''Show PDB entry.

    Examples
    --------
    >>> import nglview as nv
    >>> w = nv.show_pdbid("3pqr")
    >>> w # doctest: +SKIP
    '''
    structure = PdbIdStructure(pdbid, mirror)
    return NGLWidget(structure, **kwargs)

nglview.show_pdbid = show_pdbid
