class Calculator {
  constructor(value) {
    this.value = value;
  }

  add(value) {
    this.value += value;
    return this;
  }
  subtract(value) {
    this.value -= value;
    return this;
  }

  multiply(value) {
    this.value *= value;
    return this;
  }

  divide(value) {
    if (value == 0) {
      throw new Error("Division by zero is not allowed");
    }
    this.value /= value;
    return this;
  }

  power(value) {
    this.value **= value;
    return this;
  }

  getResult() {
    return this.value;
  }
}

const init = new Calculator(10);
console.log(init.add(5).subtract(7).getResult());
