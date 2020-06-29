"""Unit tests for C4Game.py"""

import unittest
from C4Game import *

class TestC4Game(unittest.TestCase):

	def test_init(self):
		"""Tests for C4Game.__init__ (therefore includes some testing of C4Game.createBoard and Player class"""
		game = C4Game(2, 3, 2, 1, 0, "Maya", "Joey")
		# Tests basic attributes
		self.assertEqual(game.players, 2)
		self.assertEqual(game.boardWidth, 3)
		self.assertEqual(game.boardHeight, 2)
		self.assertEqual(game.winLength, 1)
		self.assertEqual(game.turn, 0)
		self.assertEqual(len(game.playerArray), game.players)
		# Tests that playerArray comes out as expected
		player0Exp = Player(0, "Maya")
		player1Exp = Player(1, "Joey")
		self.assertEqual(game.playerArray[0].name, player0Exp.name)
		self.assertEqual(game.playerArray[0].color, player0Exp.color)
		self.assertEqual(game.playerArray[1].name, player1Exp.name)
		self.assertEqual(game.playerArray[1].color, player1Exp.color)
		# Tests that board comes out as expected
		boardExp = [['-','-','-'],['-','-','-']]
		self.assertEqual(game.board, boardExp)

	def test_play_turns(self):
		"""Tests that C4Game.play advances turns properly"""
		game = C4Game(2, 3, 4, 2, 0, "Joey", "Maya")
		self.assertEqual(game.turn, 0)
		game.play(1)
		self.assertEqual(game.turn, 1)
		game.play(2)
		self.assertEqual(game.turn, 0)
		game.play(1)
		self.assertEqual(game.turn, 1)
		game.play(3)
		self.assertEqual(game.turn, 0)

	def test_play(self):
		"""Tests that C4Game.play changes the board properly"""
		game = C4Game(2, 3, 4, 2, 0, "Maya", "Joey")
		b = colored('O', 'blue')
		r = colored('O', 'red')
		turn0Exp = [
			['-','-','-'],
			['-','-','-'],
			['-','-','-'],
			['-','-','-']
		]
		self.assertEqual(game.board, turn0Exp)
		game.play(1)
		turn1Exp = [
			[b, '-', '-'],
			['-', '-', '-'],
			['-', '-', '-'],
			['-', '-', '-']
		]
		self.assertEqual(game.board, turn1Exp)
		game.play(1)
		turn2Exp = [
			[  b,'-','-'],
			[  r,'-','-'],
			['-','-','-'],
			['-','-','-']
		]
		self.assertEqual(game.board, turn2Exp)
		game.play(2)
		turn3Exp = [
			[b, b, '-'],
			[r, '-', '-'],
			['-', '-', '-'],
			['-', '-', '-']
		]
		self.assertEqual(game.board, turn3Exp)
		game.play(3)
		turn4Exp = [
			[  b,  b,  r],
			[  r,'-','-'],
			['-','-','-'],
			['-','-','-']
		]
		self.assertEqual(game.board, turn4Exp)
		game.play(2)
		turn5Exp = [
			[  b,  b,  r],
			[  r,  b,'-'],
			['-','-','-'],
			['-','-','-']
		]
		self.assertEqual(game.board, turn5Exp)
		game.play(1)
		turn6Exp = [
			[b, b, r],
			[r, b, '-'],
			[r, '-', '-'],
			['-', '-', '-']
		]
		self.assertEqual(game.board, turn6Exp)


if __name__ == "__main__":
	unittest.main()

