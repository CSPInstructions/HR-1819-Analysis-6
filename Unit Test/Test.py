# We import the unittest library and the content of the Fac file
import unittest
import Fac

# We create a class that will contain or tests
class TestFactional( unittest.TestCase ):
    
    # We define a test case for the fac function
    def test_factional(self):

        # We wanna check whether we receive a value error
        with self.assertRaises( ValueError ):
            # We run the fac function with 0 as argument
            Fac.fac( 0 )

        # We wanna check whether we receive a value error
        with self.assertRaises( ValueError ):
            # We run the fac function with -1 as argument
            Fac.fac( -1 )

        # We wanna check whether we receive a value error
        with self.assertRaises( ValueError ):
            # We run the fac function with 'hi' as argument
            Fac.fac( "Hi" )

        # We wanna check whether we receive the right result for arguments 5 and 1
        self.assertEqual(Fac.fac(5), 120)
        self.assertEqual(Fac.fac(1), 1)


###############
# Python Crap #
###############

if __name__ == '__main__':
    unittest.main()