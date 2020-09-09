// Author Shotaro Murata

export default function calcDistance(lat1, lng1, lat2, lng2) {
    const pi = Math.PI
    const r_earth = 6378.137
    lat1 *= pi / 180
    lat2 *= pi / 180
    lng1 *= pi / 180
    lng2 *= pi / 180

    return r_earth * Math.acos(Math.cos(lat1)
        * Math.cos(lat2)
        * Math.cos(lng2 -lng1)
        + Math.sin(lat1)
        * Math.sin(lat2)
    )
}