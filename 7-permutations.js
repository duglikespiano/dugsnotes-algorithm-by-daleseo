function permute(nums) {
	const result = [];

	function dfs(picked, unpicked) {
		if (unpicked.length === 0) {
			result.push(picked);
			return;
		}

		for (let i = 0; i < unpicked.length; i++) {
			dfs([...picked, unpicked[i]], [...unpicked.slice(0, i), ...unpicked.slice(i + 1)]);
		}
	}

	dfs([], nums);
	console.log(result);
	return result;
}

permute([3, 5, 8]);
