import { Injectable } from '@angular/core';
import { UserDTO } from './User';
import { HttpClient } from '@angular/common/http';
import { Observable, lastValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private readonly urlAPI: string = 'http://localhost:8080/api/';

  constructor(
    private _http: HttpClient
  ) { }


  //--- Get Users
  public getUsers(): Promise<UserDTO[]> {
    const observable: Observable<UserDTO[]> = this._http.get<UserDTO[]>(`${this.urlAPI}user`);
    return lastValueFrom(observable);
  }

  //--- Get User By ID
  public getUserByID(id: number): Promise<UserDTO> {
    const observable: Observable<UserDTO> = this._http.get<UserDTO>(`${this.urlAPI}user/${id}`);
    return lastValueFrom(observable);
  }

  //--- Save User
  public saveUser(user: UserDTO): Promise<UserDTO> {

    const observable: Observable<UserDTO> = user.id ? 
    this._http.put<UserDTO>(`${this.urlAPI}user`, user)
    :
    this._http.post<UserDTO>(`${this.urlAPI}user`, user);
    return lastValueFrom(observable);
  }

  //--- Delete User
  public deleteUser(id: number): Promise<void> {
    const observable: Observable<void> = this._http.delete<void>(`${this.urlAPI}user/${id}`);
    return lastValueFrom(observable);
  }
}
