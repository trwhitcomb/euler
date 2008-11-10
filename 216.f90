module prime
    implicit none

    private
    
    public :: isPrime


    recursive function expmod(base, expt, m) result expm
        integer :: base
        integer :: expt
        integer :: m
        integer :: expm

        if (expt .eq. 0) then
            expm = 1
        else if (even(expt))
            expm = mod(square(expmod(base, (expt / 2), m)), m)
        else
            expm = mod(base * expmod(base, (expt - 1), m),  m)
        end if
    end function expmod

    function square(n)
        integer :: n
        integer :: square

        square = n * n
    end function square


    function fermatTest(n)
        integer :: n
        logical :: fermatTest

        real :: rand_R
        integer :: rand

        call random_number(rand_R)
        rand = int(random_number * (n - 1)) + 1
        fermatTest = expmod(rand, n, n) .eq. rand
    end function fermatTest

    function fastPrime(n, times)
        integer :: n, times
        logical :: fastPrime

        integer :: ii
        fastPrime = .true.
        do ii=1,times
            fastPrime = fastPrime .and. fermatTest(n) 
        end do
    end function fastPrime

    function isPrime(n)
        integer :: n
        logical :: isPrime

        isPrime = fastPrime(n, 10)
    end function isPrime
end module prime

program problem216

    use prime

    implicit none

    integer, parameter :: MAX_N = 10000

    integer :: nn
    integer :: primeCount = 0

    do nn = 2, MAX_N
        if (isPrime(t(nn))) primeCount = primeCount + 1
    end do

    write (*,*) "Algorithm counts", primeCount, "below", MAX_N
contains
    
    function t(n)
        integer :: n
        integer :: t

        t = 2 * n * n - 1
    end function t
end program problem216

