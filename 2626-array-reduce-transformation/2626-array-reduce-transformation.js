/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var output = init;
    nums.forEach((element) => {
        output = fn(output, element);
    });
    return output;
};