function isAnagram(string1, string2) {
	// function convertString(string) {
	// 	return string
	// 		.split('')
	// 		.map((text) => text.toLowerCase())
	// 		.sort()
	// 		.join('');
	// }
	// const convertedString1 = convertString(string1);
	// const convertedString2 = convertString(string2);

	// return convertedString1 === convertedString2;

	function createHashmap(string) {
		const hashmap = {};
		const convertedString = string.toLowerCase();
		Array.from(convertedString).forEach((text) => {
			if (!Object.hasOwn(hashmap, text)) {
				hashmap[text] = 1;
			} else {
				hashmap[text]++;
			}
		});
		return hashmap;
	}

	function checkHashmap(string, hashmap) {
		const hashmapForCheck = { ...hashmap };
		const convertedString = string.toLowerCase();
		let remaining = Object.keys(hashmapForCheck).length;

		// return inside forEach() only returns from the callback function
		for (const text of convertedString) {
			if (!Object.hasOwn(hashmapForCheck, text)) {
				return false;
			}
			hashmapForCheck[text]--;
			if (hashmapForCheck[text] === 0) {
				delete hashmapForCheck[text];
				remaining--;
			}
			if (remaining === 0) {
				return true;
			}
		}
		return false;
	}

	const hashmap = createHashmap(string1);
	const result = checkHashmap(string2, hashmap);

	return result;
}

console.log(isAnagram('anagram', 'Nagaram'));
