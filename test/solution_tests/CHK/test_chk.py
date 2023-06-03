from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_checkout_with_random_sku(self):
        assert checkout_solution.checkout('G') == -1


    def test_checkout_with_free_item_offer(self):
        assert checkout_solution.checkout('E') == -1
