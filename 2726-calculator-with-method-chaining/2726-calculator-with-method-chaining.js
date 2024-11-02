class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.output = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        this.output += value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        this.output -= value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        this.output *= value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value === 0) 
        {
            throw new Error('Division by zero is not allowed');
        }
        this.output /= value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.output = Math.pow(this.output, value);
        return this;
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.output;   
    }
}