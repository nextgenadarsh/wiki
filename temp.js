

// Component 1
componentDidMount() {
    fetchUsers([1]).then(([user]) => {
        this.setState({ user });
    });
}

// Component 2
componentDidMount() {
    fetchUsers([2]).then(([user]) => {
        this.setState({ user });
    });
}

const allids = [];

// Utility
const timer = new Date();

const fetchUsers = async (ids) => {
    allids.push(ids)

    return debounce(ids, 3000)
}

let allUsers = [];

// setInterval(() => {
//     if (allids.length > 0) {
//         fetch('uri', { method: 'POST', body: { allids } }).then(res => {
//             allUsers = res.users;
//             allids = [];
//         });
//     }
// }, 3000)

///
function debounce(ids, delay) {
    const op = fetch('uri', { method: 'POST', body: { allids } });
    return new Promise(resolve => {
        setTimeout(async () => {
            op.then(res => {
                allUsers = res.users;
                allids = [];
                const user = allUsers.find(x => x.id === ids[0])
                resolve(user);
            });
        }, delay);
    });
}
