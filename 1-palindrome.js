// function isPalindrome(string) {
// 	const convertedString = string.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');
// 	const reversedString = [...convertedString].reverse().join('');
// 	return convertedString === reversedString;
// }

function isPalindrome(string) {
	const convertedString = string.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '');
	let left = 0;
	let right = convertedString.length - 1;

	while (left < right) {
		if (convertedString[left] !== convertedString[right]) {
			return false;
		}
		left++;
		right--;
	}
	return true;
}

console.log(isPalindrome('A man, a plan, a canal: Panama'));
console.log(isPalindrome('Race a car'));
console.log(isPalindrome(' '));
