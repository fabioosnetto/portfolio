export interface UserDTO {
   id:        number | null;
   username:  string | null;
   firstName: string | null;
   lastName:  string | null;
   city:      string | null;
   state:     string | null;
   status:    string | null;
}

export class User {
   private _id:        number | null;
   private _username:  string | null;
   private _firstName: string | null;
   private _lastName:  string | null;
   private _city:      string | null;
   private _state:     string | null;
   private _status:    string | null;

   constructor (
      data?: UserDTO | null
   ) {
      this._id        = data?.id || null;
      this._username  = data?.username || null;
      this._firstName = data?.firstName || null;
      this._lastName  = data?.lastName || null;
      this._city      = data?.city || null;
      this._state     = data?.state || null;
      this._status    = data?.status || null;
   }

   public get id(): number | null { return this._id; }
   public get username(): string | null { return this._username; }
   public get firstName(): string | null { return this._firstName; }
   public get lastName(): string | null { return this._lastName; }
   public get city(): string | null { return this._city; }
   public get state(): string | null { return this._state; }
   public get status(): string | null { return this._status; }

   public set id(id: number | null) { this._id = id; }
   public set username(username: string | null) { this._username = username; }
   public set firstName(firstName: string | null) { this._firstName = firstName; }
   public set lastName(lastName: string | null) { this._lastName = lastName; }
   public set city(city: string | null) { this._city = city; }
   public set state(state: string | null) { this._state = state; }
   public set status(status: string | null) { this._status = status; }


   public get getUserDTO(): UserDTO {
      const resp: UserDTO = {
         id: this._id,
         username: this._username,
         firstName: this._firstName,
         lastName: this._lastName,
         city: this._city,
         state: this._state,
         status: this._status,
      };
      return resp;
   }
}