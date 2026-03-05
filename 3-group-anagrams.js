function groupAnagrams(strings) {
	// const anagrams = {};
	// for (const text of texts) {
	// 	const sortedText = text.split('').sort().join('');
	// 	if (!Object.hasOwn(anagrams, sortedText)) {
	// 		anagrams[sortedText] = [];
	// 	}
	// 	anagrams[sortedText].push(text);
	// }
	const anagrams = {};
	for (const word of strings) {
		const counter = new Array(26).fill(0);
		for (const char of word) {
			const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
			counter[index]++;
		}
		const key = counter.join(',');
		if (!anagrams[key]) {
			anagrams[key] = [];
		}
		anagrams[key].push(word);
	}
	return Object.values(anagrams);
}

console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']));
