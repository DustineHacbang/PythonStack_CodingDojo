var input = 173;

function generateCoinChangeObject(cents) {
    // set an object with key/value pairs, where all values are 0
    var output = {
        quarters: 0,
        dimes: 0,
        nickels: 0,
        pennies: 0
    };
    // edge case if statement to check that input is less than zero
    if (input < 0) {
        return false
    }
    // set temporary variable to store the result of our modulo calculations
    var temp = 0;
    // series of if statements with modulos inside, then change the values of our object to our temp variable
    if (cents >= 25) {
        temp = Math.floor(cents / 25);
        cents = cents % 25;
        output['quarters'] = temp;
    }
    if (cents >= 10) {
        temp = Math.floor(cents / 10);
        cents = cents % 10;
        output['dimes'] = temp;
    }
    if (cents >= 5) {
        temp = Math.floor(cents / 5);
        cents = cents % 5;
        output['nickels'] = temp;
    }
    output['pennies'] = cents;
    // if (output['quarters'] > 4) {
    return output
}
console.log(generateCoinChangeObject(input));



function convertToDoge(cents) {
    var temp = 0;
    var output = {
        doge_coins: 0
    },

    temp = cents / 20;
    output['doge'] = temp;
    return output;
}

console.log(convertToDoge(input));