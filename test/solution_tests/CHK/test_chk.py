from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_checkout_with_random_sku(self):
        assert checkout_solution.checkout('G') == -1


    def test_checkout_with_free_item_offer(self):
        assert checkout_solution.checkout('E') == 40

    def test_checkout_2(self):
        # assert checkout_solution.checkout('ABCDE') == 155
        # assert checkout_solution.checkout('AAAAA') == 200
        # assert checkout_solution.checkout('EEB') == 80
        # assert checkout_solution.checkout('EEEB') == 120
        # assert checkout_solution.checkout('EEEEBB') == 160
        # assert checkout_solution.checkout('AAAA') == 200
        assert checkout_solution.checkout('AAAAAA') == 250
        assert checkout_solution.checkout('AAAAAAA') == 300