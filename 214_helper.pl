#!/usr/bin/perl
#
# Totient chains

use Math::Prime::TiedArray;

print "Precomputing primes...\n";
tie my @primes, "Math::Prime::TiedArray", precompute => 40_000_000;
print "Done\n";

open(PRIMES,">primes.input");

my $counter = 0;
while ((my $prime = shift @primes) < 40_000_000)
{
    print PRIMES "$prime\n";
    print "$counter\t$prime\n" if ($counter++ % 10_000);
}
close(PRIMES);
