package set

type Set[T comparable] map[T]struct{}

func NewSet[T comparable](arr ...T) Set[T] {
	set := make(Set[T])
	for _, x := range arr {
		set.Add(x)
	}
	return set
}
func (set Set[T]) Add(x T) {
	set[x] = struct{}{}
}
func (set Set[T]) Remove(x T) {
	delete(set, x)
}
func (set Set[T]) Has(x T) bool {
	_, exists := set[x]
	return exists
}
func (set Set[T]) Pop() T {
	var a T
	for b := range set {
		a = b
		break
	}
	delete(set, a)
	return a
}
