; Project Euler
; Problem 108
; Diophantine Equations

(define (count-factors number end-val)
  (define (num-factors n test-val factor-count)
    (if (= test-val end-val)
        (+ 1 (* 2 factor-count))
        (if (= 0 (remainder n test-val))
            (num-factors n (- test-val 1) (+ factor-count 1))
            (num-factors n (- test-val 1) factor-count))))
  (num-factors number number 0))

(define (square x)
  (* x x))

(define (num-solutions n)
  (let ((d (count-factors (square n) n)))
    (if (= 0 (remainder d 2))
        (/ d 2)
        (/ (+ d 1) 2))))

(define (least-n-solution n-guess target)
  (cond ((= 0 (remainder n-guess 100))
         (display n-guess)
         (newline)))
  (if (> (num-solutions n-guess) target)
      n-guess
      (least-n-solution (+ 1 n-guess) target)))

(least-n-solution 1200 1000)