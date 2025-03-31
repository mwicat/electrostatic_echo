from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.osutil import ensuredir
from rdkit import Chem
from rdkit.Chem import Draw
import hashlib
import os


def setup(app):
    app.add_directive('molimage', MoleculeImage)


class MoleculeImage(Directive):
    required_arguments = 1  # SMILES string

    def run(self):
        smiles = self.arguments[0]
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            error = self.state_machine.reporter.error(
                f"Invalid SMILES string: {smiles}", nodes.literal_block('', smiles), line=self.lineno)
            return [error]

        # Generate filename based on SMILES hash
        hashname = hashlib.md5(smiles.encode()).hexdigest() + ".png"
        image_dir = os.path.join(self.state.document.settings.env.app.outdir, "_images")
        ensuredir(image_dir)
        image_path = os.path.join(image_dir, hashname)

        # Save image if not already generated
        if not os.path.exists(image_path):
            img = Draw.MolToImage(mol, size=(300, 300))
            img.save(image_path)

        # Add image node to the document
        image_node = nodes.image(uri="/_images/" + hashname)
        return [image_node]
