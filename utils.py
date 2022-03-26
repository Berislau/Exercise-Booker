import time

def highlight(web_element):
    driver = web_element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              web_element, s)
        original_style = web_element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)