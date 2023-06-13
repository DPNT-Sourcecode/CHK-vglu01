from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_checkout_with_free_item_offer(self):
        assert checkout_solution.checkout('E') == 40

    def test_checkout_2(self):
        # assert checkout_solution.checkout('ABCDE') == 155
        # assert checkout_solution.checkout('AAAAA') == 200
        # assert checkout_solution.checkout('EEB') == 80
        # assert checkout_solution.checkout('EEEB') == 120
        # assert checkout_solution.checkout('EEEEBB') == 160
        # assert checkout_solution.checkout('AAAA') == 180
        # assert checkout_solution.checkout('AAAAAA') == 250
        # assert checkout_solution.checkout('AAAAAAA') == 300
        # assert checkout_solution.checkout('BEBEEE') == 160
        # assert checkout_solution.checkout('ABCDEABCDE') == 280
        # assert checkout_solution.checkout('CCADDEEBBA') == 280
        # assert checkout_solution.checkout('AAAAAEEBAAABB') == 455
        # assert checkout_solution.checkout('ABCDECBAABCABBAAAEEAA') == 665
        # assert checkout_solution.checkout('ABCDEFF') == 175
        # assert checkout_solution.checkout('FFF') == 20
        # assert checkout_solution.checkout('FFFF') == 30
        # assert checkout_solution.checkout('FFFFFF') == 40
        # assert checkout_solution.checkout('RRRRRRQQ') == 300
        # assert checkout_solution.checkout('RRRQRQRR') == 300
        # assert checkout_solution.checkout('HHHHHHHHHH') == 80
        # assert checkout_solution.checkout('AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH') == 1610
        # assert checkout_solution.checkout('PPPPQRUVPQRUVPQRUVSU') == 730
        # assert checkout_solution.checkout('NNNNNNMM') == 240
        # assert checkout_solution.checkout('NNNMNMNN') == 240
        assert checkout_solution.checkout('WSTUKKUUXYYYYZ') == 470