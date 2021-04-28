import { createStore } from 'vuex'
import HTTP from '@/api'
// import router from '@/router'

const store = createStore({
    state: {
        accessToken: null,
        refreshToken: null,
    },
    mutations: {
        setToken: (state, model) => {
            // console.log('SetTOKENed')
            // console.log('MODEL', model)
            state.accessToken = model.access
            state.refreshToken = model.refresh
            //console.log(state.refreshToken)
        },
        clearToken: (state) => {
            state.accessToken = null
            state.refreshToken = null
        }
    },
    getters: {
        // isAuthenticated: (state) => state.accessToken.length > 0 && state.refreshToken.length > 0,

        isAuthenticated (state) {
            return state.accessToken != null
        }

    },

    actions: {
        SignIn: async ({ commit }, model) => {
            console.log('STARTED')
            HTTP.post('api/token/', model)
            .then((res) => {
                commit('setToken', res.data)
                console.log('RES DATA', res.data)
            })
        },
        SignOut: ({ commit }) => {
            commit('clearToken')
            console.log('CLEAREd')
        }
    }
})

export default store
