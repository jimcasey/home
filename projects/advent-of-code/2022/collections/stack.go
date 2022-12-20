package collections

type Stack[T any] []T

func NewStack[T any](items ...T) Stack[T] {
	stack := Stack[T]{}
	stack.Add(items...)
	return stack
}
func (stack *Stack[T]) Add(items ...T) {
	*stack = append(*stack, items...)
}
func (stack *Stack[T]) Pop() T {
	temp := *stack
	item := temp[0]
	*stack = temp[1:]
	return item
}
func (stack *Stack[T]) Length() int {
	return len(*stack)
}
