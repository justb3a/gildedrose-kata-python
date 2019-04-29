# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def create_item_and_update_quality(self, name, sellin, quality):
        item = Item(name, sellin, quality)
        GildedRose([item]).update_quality()
        return item

    def create_default_item_and_update_quality(self, sellin, quality):
        return self.create_item_and_update_quality("default", sellin, quality)

    def test_default_item_with_sellin_zero(self):
        item = self.create_default_item_and_update_quality(0, 0)
        self.assertEquals("default, -1, 0", str(item))

    def test_default_item_with_quality_positive_and_sellin_reached(self):
        item = self.create_default_item_and_update_quality(0, 3)
        self.assertEquals("default, -1, 1", str(item))

    def test_default_item_with_quality_positive_and_sellin_in_five_days(self):
        item = self.create_default_item_and_update_quality(5, 3)
        self.assertEquals("default, 4, 2", str(item))

    def test_aged_brie_increases_quality(self):
        item = self.create_item_and_update_quality("Aged Brie", 5, 3)
        self.assertEquals("Aged Brie, 4, 4", str(item))

    def test_conjured_increases_by_two_quality(self):
        item = self.create_item_and_update_quality("Conjured", 5, 3)
        self.assertEquals("Conjured, 4, 5", str(item))

    def test_aged_brie_increases_quality_never_more_than_fifty(self):
        item = self.create_item_and_update_quality("Aged Brie", 5, 50)
        self.assertEquals("Aged Brie, 4, 50", str(item))

    def test_conjured_increases_quality_never_more_than_fifty(self):
        item = self.create_item_and_update_quality("Conjured", 5, 49)
        self.assertEquals("Conjured, 4, 50", str(item))

    def test_aged_brie_increases_quality_twice_after_sellin(self):
        item = self.create_item_and_update_quality("Aged Brie", 0, 48)
        self.assertEquals("Aged Brie, -1, 50", str(item))

    def test_conjured_increases_quality_twice_after_sellin(self):
        item = self.create_item_and_update_quality("Conjured", 0, 46)
        self.assertEquals("Conjured, -1, 50", str(item))

    def test_aged_brie_increases_quality_twice_after_sellin_but_no_more_than_fifty(self):
        item = self.create_item_and_update_quality("Aged Brie", 0, 49)
        self.assertEquals("Aged Brie, -1, 50", str(item))

    def test_conjured_increases_quality_twice_after_sellin_but_no_more_than_fifty(self):
        item = self.create_item_and_update_quality("Conjured", 0, 47)
        self.assertEquals("Conjured, -1, 50", str(item))

    def test_sulfuras_does_not_change(self):
        item = self.create_item_and_update_quality("Sulfuras, Hand of Ragnaros", 0, 49)
        self.assertEquals("Sulfuras, Hand of Ragnaros, 0, 49", str(item))

    def test_sulfuras_may_have_higher_quality(self):
        item = self.create_item_and_update_quality("Sulfuras, Hand of Ragnaros", 0, 80)
        self.assertEquals("Sulfuras, Hand of Ragnaros, 0, 80", str(item))

    def test_backstage_passes_increases_quality_by_one(self):
        item = self.create_item_and_update_quality("Backstage passes to a TAFKAL80ETC concert", 11, 5)
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert, 10, 6", str(item))

    def test_backstage_passes_increases_quality_by_two(self):
        item = self.create_item_and_update_quality("Backstage passes to a TAFKAL80ETC concert", 10, 5)
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert, 9, 7", str(item))

    def test_backstage_passes_increases_quality_by_three(self):
        item = self.create_item_and_update_quality("Backstage passes to a TAFKAL80ETC concert", 5, 5)
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert, 4, 8", str(item))

    def test_backstage_passes_decreases_quality_to_zero(self):
        item = self.create_item_and_update_quality("Backstage passes to a TAFKAL80ETC concert", 0, 5)
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert, -1, 0", str(item))



if __name__ == '__main__':
    unittest.main()
