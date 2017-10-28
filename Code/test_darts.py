import darts
import unittest


class TestDarts(unittest.TestCase):
    def test_init(self):
        game  = darts.scoreboard()
    def test_score(self):
        game  = darts.scoreboard()
        self.assertEqual(game.playerscore(1),301)
        self.assertEqual(game.playerscore(2),301)
    def test_exception(self):
        game = darts.scoreboard()
        self.assertRaises(NameError, game.playerscore,3)
    def test_scoring_single(self):
        game = darts.scoreboard()
        game.playerthrown(1,'single',15)
        self.assertEqual(game.playerscore(1),301-15)
    def test_scoring_double(self):
        game = darts.scoreboard()
        game.playerthrown(1,'double',20)
        self.assertEqual(game.playerscore(1),301-(2*20))
    def test_scoring_triple(self):
        game = darts.scoreboard()
        game.playerthrown(1,'triple',5)
        self.assertEqual(game.playerscore(1),301-(3*5))
    def test_player_1_plays_first(self):
        game = darts.scoreboard()
        #If a player 2 plays before player 1 then raise an 
        self.assertRaises(NameError, game.playerthrown,2,'single',5)
    def test_three_throws_1(self):
        game = darts.scoreboard()
        game.playerthrown(1,'triple',5)
        game.playerthrown(1,'triple',5)
        game.playerthrown(1,'triple',5)
        game.playerthrown(2,'triple',20)
    def test_three_throws_2(self):
        game = darts.scoreboard()
        game.playerthrown(1,'triple',5)
        game.playerthrown(1,'triple',5)
        game.playerthrown(1,'triple',5)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
    def test_three_throws_3(self):
        game = darts.scoreboard()
        game.playerthrown(1,'double',5)
        game.playerthrown(1,'double',5)
        game.playerthrown(1,'double',5)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        self.assertEqual(game.playerscore(2),301-3*3*20)

    def test_three_throws_4(self):
        game = darts.scoreboard()
        game.playerthrown(1,'double',5)
        game.playerthrown(1,'double',5)
        game.playerthrown(1,'double',5)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        self.assertEqual(game.playerscore(2),301-3*3*20)
        self.assertEqual(game.playerscore(1),301-3*2*5)
        
    def test_three_throws_5(self):
        game = darts.scoreboard()
        game.playerthrown(1,'double',5)
        game.playerthrown(1,'double',5)
        game.playerthrown(1,'double',5)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        game.playerthrown(2,'triple',20)
        self.assertEqual(game.playerscore(2),301-3*3*20)
        self.assertEqual(game.playerscore(1),301-3*2*5)        
        game.playerthrown(1,'single',18)
        self.assertEqual(game.playerscore(1),301-3*2*5-18)

    def test_win_1(self):
        # Test what happens when we get to zero.
        game = darts.scoreboard()
        game.playerthrown(1,'triple',20)
        game.playerthrown(1,'triple',20)
        game.playerthrown(1,'triple',20)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(1,'double',19)
        game.playerthrown(1,'double',19)
        game.playerthrown(1,'double',19)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(1,'single',1)
        game.playerthrown(1,'single',3)
        game.playerthrown(1,'single',3)
        self.assertEqual(game.playerscore(1),'WON')
        
    def test_win_2(self):
        # Test what happens when we get to zero.
        game = darts.scoreboard()
        game.playerthrown(1,'triple',20)
        game.playerthrown(1,'triple',20)
        game.playerthrown(1,'triple',20)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(1,'double',19)
        game.playerthrown(1,'double',19)
        game.playerthrown(1,'double',19)
        current_score_player_1 = game.playerscore(1)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(1,'single',1)
        game.playerthrown(1,'single',3)
        game.playerthrown(1,'triple',20)
        self.assertEqual(game.playerscore(1),current_score_player_1)
        self.assertNotEqual(game.playerscore(1),'WON')
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(2,'single',1)
        game.playerthrown(1,'single',1)
        game.playerthrown(1,'single',3)
        game.playerthrown(1,'single',3)
        self.assertEqual(game.playerscore(1),'WON')

        
if __name__ == '__main__':
    unittest.main()

