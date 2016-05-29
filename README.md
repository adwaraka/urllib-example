------
NOTES
------
As a part of an interview test - still useful to keep around. Compatible with Python 2.7. No additional pip installs required.

Just run python test<the program you want to run>. 'src' contains url_parser.py code that contains two functions that make the appropriate POST requests.

The automation of Prime Numbers is split into two parts - one for a comprehensive run and the other for out-of-range scenarios and checks for specific values. Helped in triaging errors in the complete run.

For the testPrimeComplete, a 'Logs' directory gets created and inside that, a 'prime_log_<current_timestamp>.log' will get generated. I decided to grep/findstr which number was declared as a PRIME or NOT. Useful method for triaging large runs like this.
