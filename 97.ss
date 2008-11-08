; Project Euler
; Problem 97


(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))

(define (square x)
  (* x x))

; Calculate the last 10 digits of the non-Mersenne prime
(define modulus (expt 10 10))

(define a (remainder 28433 modulus))
(define b (expmod 2 7830457 modulus))
(define c (remainder 1 modulus))

(define digits
  (+ c
     (remainder (* a b) modulus)))


