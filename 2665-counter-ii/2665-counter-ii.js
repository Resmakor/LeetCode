/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let current_counter = init;
    function increment()
    {
        return ++current_counter;
    }
    function decrement()
    {
        return --current_counter;
    }
    function reset()
    {
        return (current_counter = init);
    }
    return {increment, decrement, reset};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */