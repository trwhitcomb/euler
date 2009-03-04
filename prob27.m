% Project Euler
% Problem 27

clear all;
close all;

% Consider quadratics of the form
% p = n^2 + an + b, n(a + n) + b
% that generates the maximum number of primes for consecutive values
% of n >= 0, |a|, |b| < 1000

PrimeGen = @(a, b, n) n*(a + n) + b

% When n = 0, p = b so restrict b to the set of primes below 1000
allB = primes(1000);

maxA      = 0;
maxB      = 0;
maxPrimes = 0;

for b = allB
	for a = -1000:1000
		if (a > 0)
			limit = b-a;
		else
			limit = b;
		end

		primeCount = 0;

		for n = 0:limit
			p = PrimeGen(a, b, n);
			if ((p > 0) && isprime(p))
				primeCount = primeCount + 1;
			else
				break;
			end
		end
		if (primeCount > maxPrimes)
			maxPrimes = primeCount;
			maxA = a;
			maxB = b;
			disp(sprintf('a = %d, b = %d gives %d primes', ...
			 	     a, b, primeCount));
		end
	end
end
