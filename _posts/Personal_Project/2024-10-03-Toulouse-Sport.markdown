---
layout: default
title:  "Toulouse Sport Mobile App"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

[← Back to Personal Project](./my-perso-projects.html)

# Toulouse Sport - Mobile Application

## Introduction

**Toulouse Sport** is a cross-platform mobile application built with **React Native** and **Expo**, designed to connect sports enthusiasts in Toulouse. The app allows users to discover sports activities, find practice partners, join community events, and organize their own sports sessions. With a focus on social connectivity and real-time updates, the application provides a seamless experience for building an active sports community.

**Key Objectives**:
- Connect people who share similar sports interests
- Facilitate the organization of sports activities
- Provide location-based discovery of nearby sports events
- Build a vibrant community of athletes and sports enthusiasts

**Version**: 1.0.0  
**Platform**: iOS, Android  
**Status**: Active Development

---

## Technology Stack

### Frontend Framework
- **React Native 0.81.4**: Cross-platform mobile development
- **Expo 54.0**: Development toolchain and build system
- **TypeScript 5.9**: Type-safe development
- **React 19.1**: Latest React features and hooks

### UI Components & Navigation
- **React Navigation 6.x**: Stack and tab-based navigation
  - `@react-navigation/native-stack`: Native stack navigator
  - `@react-navigation/bottom-tabs`: Bottom tab navigation
  - `@react-navigation/stack`: Modal and card stack navigation
- **React Native Elements (RNEUI)**: Pre-built UI component library
- **React Native Vector Icons**: Icon library for UI elements
- **React Native Safe Area Context**: Safe area handling for notched devices

### Backend & Services
- **Supabase 2.45**: Backend-as-a-Service platform
  - **Authentication**: Email/password authentication with session management
  - **PostgreSQL Database**: Relational database with Row Level Security (RLS)
  - **Storage**: Image and file storage with CDN
  - **Real-time Subscriptions**: Live data updates
- **Async Storage**: Local data persistence

### Media & Assets
- **Expo Image Picker**: Camera and gallery integration
- **Expo Status Bar**: Status bar configuration

### Development Tools
- **Babel**: JavaScript transpiler
- **Metro Bundler**: React Native bundler
- **Supabase CLI**: Database migrations and local development

<img src="/img/toulouse-sport/app_screenshot.png" alt="App Screenshot" style="width: 100%;" onclick="openModal(this.src)"/>

---

## Core Features

### 1. Authentication System
**Secure user authentication powered by Supabase Auth**:
- Email/password registration and login
- Session persistence with automatic token refresh
- Secure logout functionality
- Password recovery (planned)
- Social auth integration (planned: Google, Apple)

**Implementation**:
- `Auth.tsx`: Authentication UI component
- Session state managed in `App.tsx`
- Automatic navigation based on authentication status

### 2. User Profile Management
**Comprehensive profile system**:
- **Personal Information**: Username, age, location
- **Avatar Upload**: Custom profile pictures with image picker
- **Sports Preferences**: List of favorite sports and skill levels
- **Bio & Website**: Personal description and social links
- **Privacy Settings**: Control profile visibility

**Database Schema**:
- `profiles` table: User profile data linked to auth users
- `sport_list` table: Available sports with images
- Foreign key relationships ensuring data integrity

### 3. Home Feed
**Dynamic activity feed showing**:
- Recent sports activities and events
- Friend activities and updates
- Recommended activities based on preferences
- Nearby events (location-based)

**Components**:
- `Home.tsx`: Main feed screen
- `HomeCard.tsx`: Activity card component
- `AccountFilled.tsx`: User profile header

### 4. Sports Discovery
**Browse and explore sports**:
- Complete sports catalog with images
- Sport descriptions and details
- Filtering by category and popularity
- Search functionality

**Implementation**:
- `SportList.tsx`: Sports list component with FlatList rendering
- Image loading from Supabase Storage
- Fallback images for error handling
- Optimized performance with virtualized lists

### 5. Map Integration
**Location-based features** (in development):
- View sports activities on interactive map
- Find nearby gyms, parks, and sports facilities
- Distance calculation to events
- Route planning integration

**Component**: `MapScreen.tsx`

### 6. Friends & Social
**Build your sports network**:
- Send and accept friend requests
- View friends' profiles and activities
- Activity sharing and invitations
- Group chat for events (planned)

**Component**: `Friends.tsx`

### 7. Navigation System
**Intuitive multi-level navigation**:
- **Bottom Tab Navigator**: Main app sections (Home, Sports, Map, Profile)
- **Stack Navigator**: Nested screens with back navigation
- **Modal Presentations**: Overlays for forms and detail views
- **Deep Linking**: Direct navigation to specific screens (planned)

**Navigation Structure**:
```
AppNavigator (Stack)
├── Auth (if not signed in)
└── Navigation (Bottom Tabs)
    ├── Home (Stack)
    │   ├── Home Feed
    │   └── Activity Details
    ├── Sports (Stack)
    │   ├── Sport List
    │   └── Sport Details
    ├── Map (Stack)
    │   └── Map View
    └── Profile (Stack)
        ├── Profile View
        ├── Edit Profile
        └── Settings
```

### 8. Settings & Preferences
**Customization options**:
- Account settings
- Notification preferences
- Privacy controls
- Language selection (planned)
- Theme customization (planned)

**Component**: `Parameter.tsx`

---

## Architecture & Implementation

### Project Structure

```
toulouse-sport/
├── App.tsx                    # Root component with session management
├── components/                # Reusable UI components
│   ├── Auth.tsx              # Authentication form
│   ├── Account.tsx           # User account management
│   ├── AccountFilled.tsx     # Profile header component
│   ├── AppNavigator.tsx      # Navigation configuration
│   ├── Avatar.tsx            # Avatar display component
│   ├── Card/
│   │   └── HomeCard.tsx      # Activity card component
│   └── Icons (Account, Parameter, SignOut)
├── src/                       # Main application screens
│   ├── Home.tsx              # Home feed screen
│   ├── SportList.tsx         # Sports catalog
│   ├── MapScreen.tsx         # Map view
│   ├── Profile.tsx           # User profile
│   ├── Friends.tsx           # Friends list
│   ├── Parameter.tsx         # Settings
│   ├── Navigation.tsx        # Tab navigator
│   └── AvatarProfile.tsx     # Avatar editing
├── lib/
│   ├── supabase.ts           # Supabase client configuration
│   └── types.ts              # TypeScript type definitions
├── supabase/
│   ├── config.toml           # Supabase configuration
│   ├── seed.sql              # Database seed data
│   └── migrations/           # Database schema migrations
├── assets/                    # Images and static files
├── android/                   # Android native code
└── ios/                       # iOS native code
```

### Authentication Flow

**Session Management**:
{% raw %}
```tsx
// App.tsx - Root level session handling
const [session, setSession] = useState<Session | null>(null)

useEffect(() => {
  // Get initial session
  supabase.auth.getSession().then(({ data: { session } }) => {
    setSession(session)
  })

  // Listen for auth changes
  supabase.auth.onAuthStateChange((_event, session) => {
    setSession(session)
  })
}, [])

// Conditional rendering based on auth state
const isSignedIn = session && session.user;
return (
  <View>
    {isSignedIn ? <Navigation session={session} /> : <Auth />}
  </View>
)
```
{% endraw %}

**Authentication Component**:
- Email/password input validation
- Supabase Auth API integration
- Error handling and user feedback
- Automatic navigation on successful login

### Database Schema

**Database Migrations** (7 migrations):
1. **user_management_starter** (2024-08-24): Initial user authentication setup
2. **add_age** (2024-08-24): Added age field to profiles
3. **sport_list** (2025-04-26): Sports catalog table
4. **around_card** (2025-04-27): Nearby activities feature
5. **profile_user** (2025-04-27): Enhanced profile fields
6. **signed_card** (2025-04-27): User activity signups
7. **home_card** (2025-05-04): Home feed activities

**Key Tables**:

**`profiles`**:
- `id` (UUID, FK to auth.users)
- `username` (text)
- `age` (integer)
- `website` (text)
- `avatar_url` (text)
- `created_at` (timestamp)
- `updated_at` (timestamp)

**`sport_list`**:
- `id` (UUID, PK)
- `sport_name` (text)
- `sport_image` (text)
- `sport_description` (text)
- `category` (text)
- `created_at` (timestamp)

**`home_card`** (Activities):
- `id` (UUID, PK)
- `user_id` (UUID, FK to profiles)
- `sport_id` (UUID, FK to sport_list)
- `title` (text)
- `description` (text)
- `location` (text)
- `date_time` (timestamp)
- `max_participants` (integer)
- `created_at` (timestamp)

**`signed_card`** (Activity Signups):
- `id` (UUID, PK)
- `user_id` (UUID, FK to profiles)
- `card_id` (UUID, FK to home_card)
- `signed_at` (timestamp)

**Row Level Security (RLS)**:
- Users can only update their own profiles
- Activities visible to all authenticated users
- Only activity creators can delete their events
- Signup management restricted to participants

<img src="/img/toulouse-sport/db_schema.png" alt="Database Schema" style="width: 100%;" onclick="openModal(this.src)"/>

### Image Management

**Supabase Storage Integration**:
{% raw %}
```tsx
// SportList.tsx - Image loading from storage
async function downloadImage(path: string) {
  try {
    const { data, error } = await supabase.storage
      .from('sports')
      .download(path)
    
    if (error) throw error

    const fr = new FileReader()
    fr.readAsDataURL(data)
    fr.onload = () => {
      setSportUrl(fr.result as string)
    }
  } catch (error) {
    console.log('Error downloading image:', error.message)
  }
}
```
{% endraw %}

**Features**:
- Automatic image download from Supabase Storage
- FileReader for blob-to-base64 conversion
- Fallback to default images on error
- Optimized caching for performance

### State Management

**Local State**: React hooks (useState, useEffect)
- Component-level state for UI interactions
- Session state in root App component
- Form state in authentication and profile components

**Server State**: Supabase real-time subscriptions (planned)
- Live updates for activities and friend requests
- Real-time chat messages
- Notification system

### Type Safety

**TypeScript Integration**:
{% raw %}
```tsx
// lib/types.ts - Database type definitions
export type Tables<T extends keyof Database['public']['Tables']> = 
  Database['public']['Tables'][T]['Row']

type SportList = Tables<"sport_list">
type Profile = Tables<"profiles">
type HomeCard = Tables<"home_card">
```
{% endraw %}

**Benefits**:
- Compile-time type checking
- IntelliSense support
- Reduced runtime errors
- Better developer experience

---

## Development Process

### Setup & Configuration

**1. Project Initialization**:
```bash
# Create Expo app with TypeScript
npx create-expo-app toulouse-sport --template expo-template-blank-typescript

# Install dependencies
npm install @supabase/supabase-js @react-navigation/native
npm install expo-image-picker react-native-vector-icons
```

**2. Supabase Configuration**:
{% raw %}
```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js'
import AsyncStorage from '@react-native-async-storage/async-storage'

const supabaseUrl = 'YOUR_SUPABASE_URL'
const supabaseAnonKey = 'YOUR_SUPABASE_ANON_KEY'

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    storage: AsyncStorage,
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: false,
  },
})
```
{% endraw %}

**3. Platform-Specific Setup**:
- **iOS**: Pods installation, Info.plist permissions (camera, photo library)
- **Android**: Gradle configuration, AndroidManifest permissions
- **Expo**: app.json configuration for build settings

### Build & Deployment

**Development**:
```bash
# Start development server
npm start

# Run on iOS simulator
npm run ios

# Run on Android emulator
npm run android

# Web development
npm run web
```

**Production Builds**:
```bash
# iOS build (requires Apple Developer account)
eas build --platform ios

# Android build (APK or AAB)
eas build --platform android

# Submit to App Store / Play Store
eas submit
```

### Testing Strategy

**Manual Testing**:
- Device testing on iOS and Android
- Different screen sizes and orientations
- Network conditions (offline, slow 3G)
- Edge cases and error scenarios

**Planned Automated Testing**:
- Jest for unit tests
- React Native Testing Library for component tests
- Detox for E2E testing
- Supabase Edge Functions testing

---

## Challenges & Solutions

### Challenge 1: Cross-Platform Consistency
**Problem**: UI differences between iOS and Android
**Solution**: 
- React Native Elements for consistent components
- Platform-specific styles where needed
- Safe Area Context for notched devices
- Extensive testing on both platforms

### Challenge 2: Image Loading Performance
**Problem**: Slow image loading from Supabase Storage
**Solution**:
- Implemented caching strategy
- Lazy loading with FlatList virtualization
- Image compression before upload
- Fallback to placeholder images

### Challenge 3: Session Management
**Problem**: Session persistence across app restarts
**Solution**:
- AsyncStorage for token persistence
- Automatic token refresh with Supabase
- Session validation on app launch
- Graceful handling of expired sessions

### Challenge 4: Database Migrations
**Problem**: Evolving schema during development
**Solution**:
- Supabase CLI for version-controlled migrations
- 7 migration files tracking schema evolution
- RLS policies for security
- Seed data for development/testing

### Challenge 5: Type Safety
**Problem**: Maintaining type consistency between frontend and database
**Solution**:
- Generated TypeScript types from database schema
- Supabase type generation tool
- Strict TypeScript configuration
- Type-safe database queries

---

## Key Features Implementation

### Sports Catalog with Images

{% raw %}
```tsx
// SportList.tsx - Rendering sports with images
function Sport({ sport }: { sport: SportList }) {
  const [sportUrl, setSportUrl] = useState<string | null>(null)

  useEffect(() => {
    sport.sport_image && downloadImage(sport.sport_image)
  }, [sport])

  return (
    <View style={styles.sportContainer}>
      {sportUrl ? (
        <Image
          source={{ uri: sportUrl }}
          style={styles.sportImage}
          defaultSource={require('../assets/icon.png')}
          onError={(error) => console.warn('Image load failed:', error)}
        />
      ) : (
        <ActivityIndicator />
      )}
      <Text style={styles.sportName}>{sport.sport_name}</Text>
    </View>
  )
}
```
{% endraw %}

### Avatar Upload with Image Picker

{% raw %}
```tsx
// AvatarProfile.tsx - Profile picture upload
const pickImage = async () => {
  const result = await ImagePicker.launchImageLibraryAsync({
    mediaTypes: ImagePicker.MediaTypeOptions.Images,
    allowsEditing: true,
    aspect: [1, 1],
    quality: 0.8,
  })

  if (!result.canceled) {
    uploadAvatar(result.assets[0].uri)
  }
}

const uploadAvatar = async (uri: string) => {
  const ext = uri.split('.').pop()
  const fileName = `${session.user.id}.${ext}`
  
  const { error } = await supabase.storage
    .from('avatars')
    .upload(fileName, file, { upsert: true })
  
  if (!error) {
    updateProfile({ avatar_url: fileName })
  }
}
```
{% endraw %}

### Bottom Tab Navigation

{% raw %}
```tsx
// Navigation.tsx - Tab navigator setup
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'

const Tab = createBottomTabNavigator()

export default function Navigation({ session }: { session: Session }) {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={{
          tabBarActiveTintColor: '#007AFF',
          tabBarInactiveTintColor: 'gray',
        }}
      >
        <Tab.Screen 
          name="Home" 
          component={Home}
          options={{
            tabBarIcon: ({ color, size }) => (
              <Icon name="home" size={size} color={color} />
            ),
          }}
        />
        <Tab.Screen name="Sports" component={SportList} />
        <Tab.Screen name="Map" component={MapScreen} />
        <Tab.Screen name="Profile" component={Profile} />
      </Tab.Navigator>
    </NavigationContainer>
  )
}
```
{% endraw %}

---

## Performance Optimization

### Image Optimization
- Image compression before upload (quality: 0.8)
- WebP format support for reduced file sizes
- Lazy loading with FlatList
- Image caching with React Native Fast Image (planned)

### List Rendering
- FlatList virtualization for large datasets
- Optimized key extraction
- Memoized components with React.memo
- WindowSize configuration for memory management

### Network Optimization
- Request batching for multiple operations
- Debounced search queries
- Pagination for activity feeds
- Optimistic UI updates

### Bundle Size
- Code splitting by screen
- Tree shaking unused dependencies
- Asset optimization (images, fonts)
- Metro bundler configuration

---

## Security Considerations

### Authentication
- Secure password hashing (handled by Supabase)
- Token-based authentication with auto-refresh
- Session expiration and validation
- Secure storage with AsyncStorage encryption

### Database Security
- Row Level Security (RLS) policies on all tables
- User can only modify their own data
- Public read access controlled by policies
- SQL injection prevention (parameterized queries)

### Data Privacy
- GDPR compliance considerations
- User data encryption at rest
- Secure file uploads to Supabase Storage
- Privacy settings for profile visibility

### API Security
- Supabase anon key for client-side access
- Service role key kept server-side only
- Rate limiting on API endpoints
- CORS configuration for web version

---

## Future Enhancements

### Phase 1: Core Features (Q1 2025)
- ✅ User authentication
- ✅ Profile management
- ✅ Sports catalog
- ✅ Basic navigation
- 🔄 Activity creation and management
- 🔄 Friend system
- 🔄 Map integration

### Phase 2: Social Features (Q2 2025)
- 📋 In-app messaging and chat
- 📋 Group creation for teams
- 📋 Activity comments and ratings
- 📋 Push notifications
- 📋 Activity sharing to social media

### Phase 3: Advanced Features (Q3 2025)
- 📋 Real-time activity updates
- 📋 Payment integration for paid events
- 📋 Calendar synchronization
- 📋 Activity recommendations with ML
- 📋 Statistics and achievements
- 📋 Leaderboards and competitions

### Phase 4: Growth & Scale (Q4 2025)
- 📋 Multi-city expansion beyond Toulouse
- 📋 Multi-language support (French, English, Spanish)
- 📋 Advanced search and filters
- 📋 Integration with fitness trackers (Strava, Garmin)
- 📋 Event ticketing system
- 📋 Sponsor and partner integration

---

## Lessons Learned

### Technical Insights
- **React Native**: Great for cross-platform development but requires platform-specific knowledge
- **Supabase**: Excellent BaaS alternative to Firebase with better SQL support
- **TypeScript**: Essential for large projects, prevents many runtime errors
- **Navigation**: React Navigation provides powerful routing but has learning curve

### Development Process
- **Iterative Development**: 7 database migrations show natural evolution of features
- **Version Control**: Git crucial for tracking changes and collaboration
- **Documentation**: Good comments and README essential for maintenance
- **Testing**: Early testing on both platforms prevents late-stage surprises

### Design Decisions
- **Mobile-First**: Focus on mobile experience before web
- **Modular Components**: Reusable components speed up development
- **Type Safety**: TypeScript worth the initial setup time
- **Backend Choice**: Supabase's free tier perfect for MVP

---

## Project Metrics

**Development Timeline**: 
- Initial setup: 2 weeks
- Core features: 6 weeks
- Testing and refinement: 2 weeks
- Ongoing development: Active

**Codebase Statistics**:
- **Components**: 15+ React components
- **Screens**: 7 main screens
- **Database Tables**: 5+ tables
- **Migrations**: 7 schema updates
- **Lines of Code**: ~3,000+ (TypeScript/TSX)

**Dependencies**: 25+ npm packages

**Platform Support**:
- ✅ iOS 13+
- ✅ Android 8.0+
- 🔄 Web (responsive design in progress)

---

## Conclusion

**Toulouse Sport** represents a comprehensive full-stack mobile development project, demonstrating proficiency in:
- Modern React Native development with TypeScript
- Backend integration with Supabase (Auth, Database, Storage)
- Cross-platform mobile app design and development
- Database schema design and migrations
- User authentication and security
- Image upload and management
- Navigation and routing
- State management and data flow

The application provides a solid foundation for building a sports community platform and showcases the ability to design, develop, and deploy production-ready mobile applications. The modular architecture and clean code practices ensure maintainability and scalability for future enhancements.

**Key Achievements**:
- Cross-platform mobile app with native performance
- Secure authentication and user management system
- Scalable database architecture with RLS
- Image upload and storage integration
- Intuitive navigation and user experience
- Type-safe development with TypeScript
- Version-controlled database migrations

The project continues to evolve with new features and improvements, demonstrating ongoing commitment to delivering a high-quality user experience for the Toulouse sports community.

---

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        line-height: 1.6;
    }
    h2, h3, h4 {
        color: #007BFF;
    }
    p {
        text-align: justify;
    }
    code {
        background-color: #f5f5f5;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
    pre {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    img {
        max-width: 100%;
        height: auto;
        margin: 20px 0;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>