package queue

type Queue[T any] struct {
	items []T
}

func NewQueue[T any]() Queue[T] {
	return Queue[T]{[]T{}}
}
func (q *Queue[T]) Add(item T) {
	q.items = append([]T{item}, q.items...)
}
func (q *Queue[T]) Pop() T {
	item := q.items[0]
	q.items = q.items[1:]
	return item
}
func (q *Queue[T]) Length() int {
	return len(q.items)
}
