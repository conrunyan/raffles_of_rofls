import { CREATE_SESSION } from "./constants";
import hosts from "../../api/hosts";

export const createSession = (sessionInfo) => async (dispatch) => {
  console.log(sessionInfo);
  hosts.post("", {
    name: sessionInfo.hostName,
    host_token: sessionInfo.sessionName,
  });
};
