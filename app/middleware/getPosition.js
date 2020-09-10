// Author Shotaro Murata
export default function ({ $axios, store }) {
    console.log(store.state.user.userInfo)
    const success = async function (pos) {
        let data = await $axios.$post("/users/update", {
            id: store.state.user.userInfo.id,
            longitude: pos.coords.longitude,
            latitude: pos.coords.latitude
        });
        store.commit("user/updatePositon", data)
    };
    if (store.state.user.userInfo.id != null)
        navigator.geolocation.getCurrentPosition(success, fail)
}

export const fail = function (error) {
    alert(error.message);
}
