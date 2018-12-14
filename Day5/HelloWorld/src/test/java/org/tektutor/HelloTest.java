package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;


public class HelloTest {

	@Test
	public void testSayHello() {

		Hello obj = new Hello();

		String actualResult = obj.sayHello();
		String expectedResult = "Hello World!";

		assertEquals ( expectedResult, actualResult );

	}

}
