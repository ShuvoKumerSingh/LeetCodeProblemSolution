var maximumWealth = function(accounts) {

    let outputs = 0;
    accounts.forEach(elements => {
        let sum = 0;
        for(element of elements)
        {
            sum+=element;
        }
        if (sum>outputs)
        {
            outputs = sum ;
        }
    });
    return outputs
    
};

let accounts = [[2,8,7],[7,1,3],[1,9,5]]

console.log(maximumWealth(accounts));