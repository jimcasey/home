package collections

type Set[T comparable] map[T]struct{}

func NewSet[T comparable](items ...T) Set[T] {
	set := make(Set[T])
	for _, item := range items {
		set.Add(item)
	}
	return set
}
func (set Set[T]) Add(item T) {
	set[item] = struct{}{}
}
func (set Set[T]) Remove(item T) {
	delete(set, item)
}
func (set Set[T]) Has(item T) bool {
	_, exists := set[item]
	return exists
}
func (set Set[T]) Pop() T {
	var item T
	for find := range set {
		item = find
		break
	}
	delete(set, item)
	return item
}
func (set Set[T]) Copy() Set[T] {
	copy := make(Set[T])
	for item := range set {
		copy.Add(item)
	}
	return copy
}
