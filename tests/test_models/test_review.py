#!/usr/bin/env python3
import unittest
from review import Review

class TestReview(unittest.TestCase):
    
    def test_initial_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
    
    def test_custom_attributes(self):
        place_id = "123"
        user_id = "456"
        text = "This is a great place!"
        review = Review(place_id=place_id, user_id=user_id, text=text)
        
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, text)
    
    def test_inheritance(self):
        review = Review()
        self.assertTrue(isinstance(review, Review))
    
    def test_base_model_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
    
    def test_custom_methods(self):
        review = Review()
        # Add your custom method tests here
        
if __name__ == '__main__':
    unittest.main()
