import json
import subprocess
import unittest


class SearchTestCase(unittest.TestCase):
    def run_search(self, terms):
        return subprocess.run(f"python search.py {terms} --json", shell=True, stdout=subprocess.PIPE)

    def test_prada_jumper(self):
        result = self.run_search("Prada jumper")

        print(result.stdout)

        data = json.loads(result.stdout)

        # There are not Prada jeans, so this should return none
        self.assertEquals(data, [])

    def test_asos_skinny_jeans(self):
        result = self.run_search("Asos skinny jeans")

        print(result.stdout)

        data = json.loads(result.stdout)

        # Asos has no skinny jeans, so display skinny jeans
        self.assertEquals(data, [
            {"id": 20828, "name": "Wet look skinny jeans", "brand": "Label Lab"},
            {"id": 1302, "name": "Black 'Antonio' skinny jeans", "brand": "Red Herring"},
            {"id": 51134, "name": "Gwenevere high-rise skinny jeans", "brand": "7 For All Mankind"},
            {"id": 37962, "name": "Low-rise skinny jeans", "brand": "Victoria Beckham Denim"},
            {"id": 8296, "name": "Blue zip pocket skinny jeans", "brand": "J by Jasper Conran"},
            {"id": 42461, "name": "Empire waxed mid-rise skinny jeans", "brand": "Levi's Made & Crafted"},
            {"id": 47903, "name": "Super skinny jeans aged pink", "brand": "Ksubi"},
            {"id": 20969, "name": "Alice smu skinny jeans", "brand": "Firetrap"},
            {"id": 11390, "name": "Clicquot skinny stretch-corduroy jeans", "brand": "Paul & Joe"},
            {"id": 6706, "name": "Dark blue skinny jeans", "brand": "Red Herring"},
            {"id": 28964, "name": "Rocket skinny jeans", "brand": "Citizens of Humanity"},
            {"id": 4296, "name": "Rocket high-rise skinny jeans", "brand": "Citizens of Humanity"},
            {"id": 12759, "name": "Ultra\u2013skinny jeans", "brand": "Warehouse"},
            {"id": 25727, "name": "Superswirl leather-stitched mid-rise skinny jeans", "brand": "Superfine"},
            {"id": 8900, "name": "811 skinny jeans", "brand": "J Brand Jeans"},
            {"id": 20982, "name": "Merc skinny jeans", "brand": "Firetrap"},
            {"id": 33923, "name": "Teeco skinny jeans", "brand": "Ted Baker"},
            {"id": 51175, "name": "The Ankle mid-rise skinny jeans", "brand": "CURRENT/ELLIOTT"},
            {"id": 41427, "name": "Mid-rise corduroy skinny jeans", "brand": "Vince"},
            {"id": 22836, "name": "Natural waist skinny jeans", "brand": "Mango"},
            {"id": 54194, "name": "Roxanne skinny jeans", "brand": "7 For All Mankind"},
            {"id": 19313, "name": "Thompson high-rise skinny jeans", "brand": "Citizens of Humanity"},
            {"id": 32296, "name": "Houlihan skinny cargo jeans", "brand": "J Brand Jeans"},
            {"id": 37431, "name": "Wonder skinny solid black jeans", "brand": "Salsa"},
            {"id": 1304, "name": "Blue high waisted skinny jeans", "brand": "Red Herring"},
            {"id": 19214, "name": "Vegas skinny jeans", "brand": "Wrangler Jeans"},
            {"id": 13224, "name": "Panelled super skinny jeans", "brand": "Label Lab"},
            {"id": 2878, "name": "Low-rise cropped skinny jeans", "brand": "Dolce & Gabbana"},
            {"id": 24062, "name": "Wet look skinny jeans", "brand": "Label Lab"},
            {"id": 14262, "name": "Carrie skinny jeans", "brand": "Beg Borrow or Steal"},
            {"id": 17582, "name": "Ultra skinny jeans", "brand": "Warehouse"},
            {"id": 19314, "name": "Thompson high-rise skinny jeans", "brand": "Citizens of Humanity"},
            {"id": 28075, "name": "Dark blue triple jet pocket skinny jeans", "brand": "J Jeans by Jasper Conran"},
            {"id": 53187, "name": "Alice skinny jeans", "brand": "Firetrap"},
            {"id": 59393, "name": "Houlihan skinny cargo jeans", "brand": "J Brand Jeans"},
            {"id": 61878, "name": "Jesse skinny jeans", "brand": "Firetrap"},
            {"id": 9391, "name": "The Floyd high-rise skinny jeans", "brand": "CURRENT/ELLIOTT"},
            {"id": 40882, "name": "Bamboo mid-rise skinny jeans", "brand": "Notify"},
            {"id": 8886, "name": "The Stiletto low-rise cropped skinny jeans", "brand": "CURRENT/ELLIOTT"},
            {"id": 40875, "name": "Dirty Boy low-rise distressed skinny jeans", "brand": "Bess"},
            {"id": 37982, "name": "612 low-rise skinny corduroy jeans", "brand": "J Brand Jeans"},
            {"id": 12817, "name": "Twist Ankle Zip wax-coated skinny jeans", "brand": "Victoria Beckham Denim"},
            {"id": 62685, "name": "Jodie skinny jeans", "brand": "True Religion"}])
