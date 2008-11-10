(define (square x)
  (* x x))

(define (sum-of-squares n)
  (/ (* n (+ n 1) (+ (* 2 n) 1)) 6))

(define (square-of-sum n)
  (/ (* (square n) (square (+ n 1))) 4))
