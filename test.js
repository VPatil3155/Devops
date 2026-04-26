const { Builder, By } = require('selenium-webdriver');

(async function testAddition() {
    let driver = await new Builder().forBrowser('chrome').build();

    try {
        await driver.get('file:///C:/Users/Vaibhav/OneDrive/Desktop/Devops/index.html');

        await driver.findElement(By.id('num1')).sendKeys('5');
        await driver.findElement(By.id('num2')).sendKeys('3');

        await driver.findElement(By.tagName('button')).click();

        let result = await driver.findElement(By.id('result')).getText();

        if (result.includes('8')) {
            console.log("Test Passed");
        } else {
            console.log("Test Failed");
        }

    } finally {
        await driver.quit();
    }
})();