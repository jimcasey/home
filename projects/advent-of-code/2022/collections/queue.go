package collections

type Queue[T any] []T

func NewQueue[T any](items ...T) Queue[T] {
	queue := Queue[T]{}
	queue.Add(items...)
	return queue
}
func (queue *Queue[T]) Add(items ...T) {
	temp := *queue
	for _, item := range items {
		temp = append([]T{item}, temp...)
	}
	*queue = temp
}
func (queue *Queue[T]) Pop() T {
	temp := *queue
	item := temp[0]
	*queue = temp[1:]
	return item
}
func (queue *Queue[T]) Length() int {
	return len(*queue)
}
