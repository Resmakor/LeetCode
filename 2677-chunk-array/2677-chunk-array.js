/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    var counter = 0;
    var output = [], temp_list = [];
    for (var i = 0; i < arr.length; i++)
    {
        temp_list.push(arr[i]);
        counter++;
        if (counter == size)
        {
            output.push(temp_list);
            temp_list = [];
            counter = 0;
        }
    }
    if (counter != 0)
        {
            output.push(temp_list);
        }
    return output;
};
