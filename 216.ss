; Project Euler
; Problem 216

; Look at the primality of numbers of the form
; t(n) = 2 * n^2 - 1, n > 1
(define (t n)
  (- (* 2 (square n)) 1))

(define (prob-216 n-max)
  (define (count-primes n-current n-max count)
    (if (> n-current n-max)
        count
        (if (is-prime? (t n-current))
            (count-primes (+ n-current 1) n-max (+ count 1))
            (count-primes (+ n-current 1) n-max count))))
  (count-primes 2 n-max 0))

(define (square x)
  (* x x))

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))  

(define (fermat-test n)
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
  (cond ((= times 0) true)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else false)))
(define (is-prime? n)
  (fast-prime? n 10))

