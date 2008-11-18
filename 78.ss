; Project Euler
; Problem 78

; Number of ways that coins can be separated into piles
(define (cc amount coin-values)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (no-more? coin-values)) 0)
        (else
         (+ (cc amount
                (except-first-denomination coin-values))
            (cc (- amount
                   (first-denomination coin-values))
                coin-values)))))

(define (first-denomination coins)
  (car coins))
(define (except-first-denomination coins)
  (cdr coins))
(define (no-more? coins)
  (null? coins))

(define (range-list n)
  (if (= n 0)
      '()
      (append (list n)
              (range-list (- n 1)))))

(define (combo n)
  (cc n (range-list n)))

(define (euler-78)
  (define (try-n n)
    (cond ((= 0 (remainder n 10))
           (display n)
           (newline)))
    (if (= 0 (remainder (combo n) 1000000))
        n
        (try-n (+ n 1))))
  (try-n 1))

(euler-78)