split = document.body.innerText.split('\n')
[...Array(split.length).keys()].filter(i=>split[i][(i * 3) % split[0].length] === '#').length
[[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]].map(([right, down])=>[...Array(split.length).keys()].filter(i=>(split[i * down] || '')[(i * right) % split[0].length] === '#').length).reduce((a, b)=>a * b, 1)
